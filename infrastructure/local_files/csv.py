import csv


class FileNotWritableException(BaseException):
	pass


def update_csv(file_path, content):
	try:
		with open(file_path, mode='w', newline='') as file:
			writer = csv.writer(file)
			writer.writerows(content)
	except FileNotWritableException:
		print('[ERROR] The file could not be opened for writing: ', file_path)


def read_csv(file_path):
	try:
		with open(file_path, mode='r', newline='') as file:
			reader = csv.reader(file)
			headers = next(reader)
			print('Headers:', headers)

			for row in reader:
				print(row)
	except FileNotFoundError:
		print('[ERROR] The file could not be opened for writing: ', file_path)