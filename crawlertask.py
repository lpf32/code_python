#!/usr/bin/python
#coding:utf8
__author__ = 'zhangpanpan'

import multiprocessing
import shutil
from optparse import OptionParser
import os
import httplib
from BeautifulSoup import BeautifulSoup
import Queue
import urllib

host = "book.douban.com"
base_url = "/tag/"

default_dir = os.path.join(os.path.curdir, "douban")
option_parse = OptionParser()
option_parse.add_option("-d", "--destination",
                        action="store", type="string", dest="destination", default=default_dir)
option_parse.add_option("-p", "--process",
                        action="store", type="int", dest="process", default=multiprocessing.cpu_count())
option_parse.add_option("-s", "--sleep", action="store", type="int", dest="sleep", default= 60 * 3)




class CrawlerTask(multiprocessing.Process):
    def __init__(self, tid, host, base_url, parent_destination, task_queue, task_sleep):
        """
        :param tid:
        :param host:
        :param base_url:
        :param parent_destination:
        :param task_queue:
        :param task_sleep:
        :return:
        """
        super(CrawlerTask, self).__init__()
        self.tid = tid
        self.host = host
        self.base_url = base_url
        self.parent_destination = parent_destination
        self.task_queue = task_queue
        self.task_sleep = task_sleep

        self.http_connection = httplib.HTTPSConnection(host)

        print "start the process %s" % self.tid

    def run(self):
        task = self.task_queue.get()
        while task:
            task_folder = os.path.join(self.parent_destination, task[1])
            href = task[0]
            url = href[len(self.host)+1:].encode('utf8')
            if not os.path.exists(task_folder):
                os.makedirs(task_folder)
            while True:
                soup, response = None, None
                try:
                    self.http_connection.request("GET", url)
                    response = self.http_connection.getresponse()
                    soup = BeautifulSoup(response.read())
                    break
                except:
                    print "Fail to connection to download the img"
                    self.http_connection.close()
                    self.http_connection = httplib.HTTPSConnection(self.host)


            items = soup.findAll('a', {"target":"_blank"})
            for item in items:
                img = item.find("img")
                src = img["src"]
                file_name = src[src.rfind('/'+1):]
                img_path = os.path.join(task_folder, file_name)
                try:
                    urllib.urlretrieve(src, img_path)
                    print "Successfully to download the image %s" % img_path
                except:
                    print "Fail to download the image"


        try:
            task = self.task_queue.get(False)
        except Queue.Empty:
            print "no task in queue"
            self.http_connection.close()








def main():
    options, args = option_parse.parse_args()

    if os.path.exists(options.destination):
        shutil.rmtree(options.destination)

    os.makedirs(options.destination)
    task_queue = multiprocessing.Queue(options.process)

    http_connection = None
    douban_host = "www.douban.com"
    task = {}
    for i in range(options.process):
        crawler_task = CrawlerTask(i, douban_host, base_url, options.destination, task_queue, options.sleep)
        task[i] = crawler_task
        crawler_task.start()

    try:
        print "Collect tasks from master"
        http_connection = httplib.HTTPSConnection(host)
        http_connection.request("GET", base_url)
        response = http_connection.getresponse()
        soup = BeautifulSoup(response.read())
        a_tags = soup.findAll("a", {"class":"tag"})

        for a in a_tags:
            task_queue.put([a["href"][7:], a.contents[0]])
            print "add task [%s, %s] into the queue" % (a["href"][8:], a.contents[0])


    except httplib.HTTPException:
        print "error"
    finally:
        if http_connection:
            http_connection.close()

    for key in task:
        task[key].join()




if __name__ == "__main__":
    main()




