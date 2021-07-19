import argparse
import json
import jbxapi

parsed = argparse.ArgumentParser()
parsed.add_argument("apikey",type=str)
parsed.add_argument("filepath",type=str)
parsed.add_argument("time",type=str, default='360')
parsed.add_argument("comment",type=str, default="bulk uploaded file")
parsed = parsed.parse_args()

jbx = jbxapi(apikey=parsed.apikey)
with open(parsde.fileath, 'rb') as file:
 print(json.dumps(jbx.submit_sample(file, params={'comments':parsed.comments, 'analysis-time':parsed.time})))
