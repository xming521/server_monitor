# Windows
import psutil as p


def main():
    with open('../process.conf', 'r', encoding='UTF-8') as f:
        read_list = eval(f.read())
    with open('../process_moreinfo.conf', 'r', encoding='UTF-8') as f:
        more_list = eval(f.read())
    all_result = []
    id = 1
    for i in read_list:
        try:
            process = p.Process(read_list[i])
            list_port = [tuple(i[3])[1] for i in process.connections('tcp')]
            result_dict = {
                'id': id,
                'name': i,
                'run': True,
                'memory': round(process.memory_info().rss / 1024 / 1024, 2),
                'net': list_port,
                'more': more_list.get(i)
            }
        except p.NoSuchProcess:
            result_dict = {
                'id': id,
                'name': i,
                'run': False,
                'more': more_list.get(i)
            }
        finally:
            id = id + 1
            all_result.append(result_dict)
    return all_result
