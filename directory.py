test_json = {
    "name": "root",
    "type": "directory",
    "children": [
        {
            "name": "file1.txt",
            "type": "file",
            "size": 1200
        },
        {
            "name": "subdir1",
            "type": "directory",
            "children": [
                {
                    "name": "file2.txt",
                    "type": "file",
                    "size": 300
                },
                {
                    "name": "file3.txt",
                    "type": "file",
                    "size": 500
                }
            ]
        },
        {
            "name": "subdir2",
            "type": "directory",
            "children": [
                {
                    "name": "subdir3",
                    "type": "directory",
                    "children": [
                        {
                            "name": "file4.txt",
                            "type": "file",
                            "size": 700
                        }
                    ]
                }
            ]
        }
    ]
}


def find_size(inp_json):
    if inp_json.get('type') == 'file':
        print(inp_json['size'])

    elif inp_json.get('type') == 'directory':
        for child in inp_json['children']:
            find_size(child)


find_size(test_json)
