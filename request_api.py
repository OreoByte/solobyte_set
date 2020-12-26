#!/usr/bin/python3

import argparse
import requests
import json

args = argparse.ArgumentParser()

args.add_argument("-t", "--target", required=True,
	help="Target/RHOST: <Domain-Name> OR <IP-Adress>, with the correct Port-Number")
args.add_argument("-o", "--option", required=True,
	help="Request Option: json (JSON API Query <-p or --path> is requried with json), OR http  <-r/--request HTTP-Request-Method>")
args.add_argument("-p", "--path", required=False,
	help="Web-directory-path, This is not required")
args.add_argument("-r", "--request", required=False,
	help="Web-Request-Method <get, post, head, or delete>")
args.add_argument("-v", "--value", required=False,
	help="Request <Value> for a JSON Webserver")

input = vars(args.parse_args())
rhost = input['target']
request = input['option']
web_path = input['path']
http_method = input['request']
value = input['value']

def json_null_val(rhost,web_path):
	value = ""
	while 1:
		response = requests.get(rhost+web_path)
		dict_data = json.loads(response.text)
		web_path = dict_data["next"]
		if web_path == "end":
			break
		value = value + dict_data["value"]
	print(value)
def json_val(rhost,web_path,value):
	while 1:
		response = requests.get(rhost+web_path)
		dict_data = json.loads(response.text)
		web_path = dict_data["next"]
		if web_path == "end":
			break
		value = value + dict_data["next"]
	print(value)
if request == "json":
	# JSON Webserver query
	if value:
		json_val(rhost,web_path,value)
	else:
		json_null_val(rhost,web_path)
elif request == "http":
	if http_method == "get":
	# get-request, to retrieve info from the taget server
		if rhost and web_path:
			get_req = requests.get(rhost+web_path)
			status_code = get_req.status_code
			text = get_req.text
		if rhost:
			get_req = requests.get(rhost)
			status_code = get_req.status_code
			text = get_req.text
			print(get_req)
			print(status_code)
			print(text)
	elif http_method == "post":
	# post-request, to send data to a target server with post-request
		if rhost and web_path:
			post_obj = {'somekey': 'somevalue'}
			post_req = requests.post(rhost+web_path, data = post_obj)
			status_code = post_req.status_code
			text = post_req.text
		if rhost:
			post_obj = {'somekey': 'somevalue'}
			post_req = requests.post(rhost, data = post_obj)
			status_code = post_req.status_code
			text = post_req.text
			print(post_req)
			print(status_code)
			print(text)
	elif http_method == "head":
	# head-request, when you don't need any file contents only the status_code or HTTP-header
		if rhost and web_path:
			head_req = requests.head(rhost+web_path)
			status_code = head_req.status_code
			text = head_req.text
		if rhost:
			head_req = requests.head(rhost)
			status_code = head_req.status_code
			text = head_req.text
			print(head_req)
			print(status_code)
			print(text)
	elif http_method == "delete":
	# delete-request, request to delete a resource from the target server
		if rhost and web_path:
			delete_req = requests.delete(rhost+web_path)
			status_code = delete_req.status_code
			text = delete_req.text
		if rhost:
			delete_req = requests.delete(rhost)
			status_code = delete_req.status_code
			text = delete_req.text
			print(delete_req)
			print(status_code)
			print(text)
	else:
		print('ERROR: No HTTP-Request Method was slec')
else:
	print('SNAFU == SoloByte')
