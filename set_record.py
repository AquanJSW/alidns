#!/usr/bin/env python
# coding=utf-8

import argparse

from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import \
    UpdateDomainRecordRequest
from aliyunsdkcore.client import AcsClient


def argparser():
    parser = argparse.ArgumentParser(description="Set record.")
    parser.add_argument("-i", "--access-key-id", type=str, required=True)
    parser.add_argument("-s", "--access-secret", type=str, required=True)
    parser.add_argument("-S", "--server", type=str, required=False,
                        choices=("qingdao", "beijing", "wulanchabu",
                                 "huhehaote", "zhangjiakou", "shanghai",
                                 "hangzhou", "shenzhen", "chengdu", "hongkong"),
                        default="hangzhou")
    parser.add_argument("-r", "--record-id", type=str, required=True,
                        help="Which could be get through `get record list`.")
    parser.add_argument("-R", "--RR", type=str, required=True,
                        help="Like '@'.")
    parser.add_argument("-t", "--type", type=str, required=True,
                        help="Like 'A', 'AAAA', 'CNAME', etc.")
    parser.add_argument("-v", "--value", type=str, required=True,
                        help="New value to assign.")
    return parser.parse_args()


def main(args):
    client = AcsClient(ak=args.access_key_id,
                       secret=args.access_secret,
                       region_id="cn-" + args.server)

    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')

    request.set_RecordId(args.record_id)
    request.set_RR(args.RR)
    request.set_Type(args.type)
    request.set_Value(args.value)

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


if __name__ == '__main__':
    main(argparser())
