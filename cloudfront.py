import csv
import json
import logging
import time
import hashlib
import os
import zlib
import urllib
import boto3

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

logging.getLogger().setLevel(logging.INFO)

key = 'E1ZKXRAA4J0BQG.2017-02-27-00.08bf0671.gz'
bucket = 'cloudfront-logs-to-kinesis-s3logbucket-ddriqzhcnb84'
response = s3.get_object(Bucket=bucket, Key=key)


def decompress_object(s3_object):
    decompressed_data = zlib.decompress(s3_object.read(), 16 + zlib.MAX_WBITS)
    return decompressed_data


def process_log_file(key, content):
    # Parse the log file into a dict and add orgin an timestamp
    kinesis_records = []
    rows = csv.reader(content.splitlines(), delimiter=' ', quotechar='"')
    iterrows = iter(rows)
    next(iterrows)
    next(iterrows)
    for index, row in enumerate(rows):
        for element in row:
            list_of_raw_elements = element.split('\t')
            if len(list_of_raw_elements) > 23:
                # generate timestamp for index
                index_time = list_of_raw_elements[0] + "T" + list_of_raw_elements[1] + "Z"
                # generate stable id in case of re-processing
                stable_event_id = hashlib.sha224("{0}.{1}".format(key, index)).hexdigest()
                log = {
                    '@timestamp': index_time,
                    'origin': 'cloudfront',
                    'logdate': list_of_raw_elements[0],
                    'logtime': list_of_raw_elements[1],
                    'edge-location': list_of_raw_elements[2],
                    'src-bytes': list_of_raw_elements[3],
                    'ip': list_of_raw_elements[4],
                    'method': list_of_raw_elements[5],
                    'host': list_of_raw_elements[6],
                    'uri-stem': list_of_raw_elements[7],
                    'status': list_of_raw_elements[8],
                    'referer': list_of_raw_elements[9],
                    'user-agent': list_of_raw_elements[10],
                    'uri-query': list_of_raw_elements[11],
                    'cookie': list_of_raw_elements[12],
                    'edge-result-type': list_of_raw_elements[13],
                    'edge-request-id': list_of_raw_elements[14],
                    'host-header': list_of_raw_elements[15],
                    'protocol': list_of_raw_elements[16],
                    'resp-bytes': list_of_raw_elements[17],
                    'time-taken': list_of_raw_elements[18],
                    'forwarded-for': list_of_raw_elements[19],
                    'ssl-protocol': list_of_raw_elements[20],
                    'ssl-cipher': list_of_raw_elements[21],
                    'edge-response-result-type': list_of_raw_elements[22],
                    'protocol-version': list_of_raw_elements[23]
                }
                logging.debug("log: %s", json.dumps(log))

                kinesis_records.append({
                    'Data': json.dumps(log, sort_keys=True),
                    'PartitionKey': stable_event_id
                })

            else:
                raise Exception('Invalid cloudfront log line {0}'.format(list_of_raw_elements))
    return kinesis_records

#print(process_log_file(key, decompress_object(response.get('Body'))))
body = '#Version: 1.0\n#Fields: date time x-edge-location sc-bytes c-ip cs-method cs(Host) cs-uri-stem sc-status cs(Referer) cs(User-Agent) cs-uri-query cs(Cookie) x-edge-result-type x-edge-request-id x-host-header cs-protocol cs-bytes time-taken x-forwarded-for ssl-protocol ssl-cipher x-edge-response-result-type cs-protocol-version\n2017-02-27\t00:00:01\tSFO5\t871\t11.222.88.188\tGET\tdata.net\t/pic/test\t404\thttps://www.test.de/\tMozilla\t-\t-\tError\t123\tpic.test.de\thttps\t235\t0.541\t-\tTLSv1.2\tECDHE-SHA256\tError\tHTTP/2.0\n'
#print(decompress_object(response.get('Body')))
print(process_log_file(key, body))