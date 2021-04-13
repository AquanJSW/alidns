#!/usr/bin/env python3
# coding=utf-8

import argparse

from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import \
    DescribeDomainRecordsRequest
from aliyunsdkcore.client import AcsClient


def argparser():
    parser = argparse.ArgumentParser(description="Get record list.")
    parser.add_argument("-i", "--access-key-id", type=str, required=True)
    parser.add_argument("-s", "--access-secret", type=str, required=True)
    parser.add_argument("-S", "--server", type=str, required=False,
                        choices=("qingdao", "beijing", "wulanchabu",
                                 "huhehaote", "zhangjiakou", "shanghai",
                                 "hangzhou", "shenzhen", "chengdu", "hongkong"),
                        default="hangzhou")
    parser.add_argument("-d", "--domain", type=str, required=True)
    return parser.parse_args()


def main(args):
    client = AcsClient(ak=args.access_key_id,
                       secret=args.access_secret,
                       region_id="cn-" + args.server)

    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')

    request.set_DomainName(args.domain)

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


if __name__ == '__main__':
    main(argparser())
