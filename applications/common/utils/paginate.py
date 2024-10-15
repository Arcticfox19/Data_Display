def paginate(data, page=1, page_size=10):
    page_count = (len(data) + page_size - 1) // page_size
    start_idx = (page - 1) * page_size
    end_idx = min(start_idx + page_size, len(data))
    page_data = data[start_idx:end_idx]

    result = {
        'page': page,
        'pageSize': page_size,
        'page_count': page_count,
        'data': page_data
    }

    return result