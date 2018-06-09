import sys, os
try:
	import git
except ImportError:
	log.debug('local_settings failed to import', exc_info=True)
	sys.exit(0)



repo = git.Repo('.')
repo.git.log(p=True)

repo.tags 							# ARRAY: [<git.TagReference "refs/tags/1.0.0">, <git.TagReference "refs/tags/develop/1.0.0">]
repo.git.tag(l=True)				# STRING: u'1.0.0\ndevelop/1.0.0'
repo.git.tag(l=True).split('\n')	# [u'1.0.0', u'develop/1.0.0']

# unicode string
log = repo.git.log('--pretty=tformat:%s')
# http://stackoverflow.com/questions/14618022/how-does-git-log-since-count
log = repo.git.log('--since=2016-10-01 23:00:00', '--pretty=tformat:%s')
log = repo.git.log('develop/1.0.0..HEAD', '--pretty=tformat:%an: %s')
log = repo.git.log('23283b7e261104234571be06543ad37d80be5ae9..HEAD', '--pretty=tformat:%ai %an: %s')

params = ['--since=2016-10-01', '--pretty=tformat:%s']
log = repo.git.log(*params)


# array
log.split('\n')

# checkout
repo.git.checkout('develop')	# branch name or tag name


def is_valid_environ_key(key):
	if os.environ.has_key(key) and os.environ[key] != '':
		return True
	else:
		return False

def get_git_commit_messages(params):
	'''
	return git commit message in string
	'''
	return repo.git.log(*params)

def main():
	params = ['--pretty=tformat:%s']

	previous_commit = os.environ['GIT_PREVIOUS_COMMIT']
	git_branch      = os.environ['GIT_BRANCH']
	is_valid_branch = ('master' not in git_branch and 'release' not in git_branch)

	commit_messages = get_git_commit_messages(params)


if __name__ == '__main__':
	main()

