# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        print('----------------------')
        moviename = item['moviename']
        movietype = item['movietype']
        showtime = item['showtime']
        output = f'{moviename}\t{movietype}\t{showtime}\n'
        with open('./maoyanmovie.csv','a+',encoding='utf-8') as maoyanmovielist:
            maoyanmovielist.write(output)
        return item
