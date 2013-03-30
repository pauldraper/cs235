import argparse
import mechanize
import re
import sys

# (SENSITIVE!) Authentication info
# Replace username and password string with correct info
try:
	from secret import username, password
except ImportError:
	username, password = r'username', r'password'

# Command line arguments
parser = argparse.ArgumentParser(description='Submit lab to CS 235 site (Winter 2013)')
parser.add_argument('lab_num', help='Lab submission number')
parser.add_argument('file_name', help='Submission file (zip)')
args = parser.parse_args()

# Go to login site
br = mechanize.Browser()
br.open('https://cas.byu.edu/cas/login?service=https%3a%2f%2fbeta.cs.byu.edu%2f~sub235%2fsubmit.php')

# Login and forward to submission site
br.form = br.forms().next()
br['username'] = username
br['password'] = password
br.submit()

# Submit
br.form = br.forms().next()
br['labnum'] = list(args.lab_num)
br.add_file(open(args.file_name), 'application/zip', args.file_name)
r = br.submit()

# Output
for h in re.findall('<h4>(.+?)</?h4>', r.read()):
	print h
