# Windows
import psutil as p


def main():
    with open('../process.conf', 'r', encoding='UTF-8') as f:
        read_list = eval(f.read())
    all_result = []
    id = 1
    for i in read_list:
        try:
            process = p.Process(read_list[i])
            result_dict = {
                'id': id,
                'name': i,
                'run': True,
                'memory': process.memory_info().rss / 1024 / 1024,
                'net': process.connections(kind="inet")
            }
        except p.NoSuchProcess:
            result_dict = {
                'id': id,
                'name': i,
                'run': False
            }
        finally:
            id = id + 1
            all_result.append(result_dict)
    return all_result
