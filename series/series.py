def slices(series, length):
	if length <= 0 or length > len(series):
		raise ValueError('length is invalid')

	return [series[i: i+length] for i in range(0, len(series) - length + 1)]
