import os
_handle_postfix = ['xls', 'xlsx']
def _enumerate_filename(pathname):
    '''
    读取所有文件名
    '''
    _filename_list = list()
    full_pathname = os.path.abspath(pathname)
    if os.path.isfile(full_pathname):
        if _is_legal_postfix(full_pathname):
            _filename_list.append(full_pathname)
        else:
            raise TypeError('文件 {} 后缀名不合法！仅支持如下文件类型：{}。'.format(pathname, '、'.join(_handle_postfix)))
    elif os.path.isdir(full_pathname):
        for relpath, _, files in os.walk(full_pathname):
            for name in files:
                filename = os.path.join(full_pathname, relpath, name)
                if _is_legal_postfix(filename):
                    _filename_list.append(os.path.join(filename))
    else:
        raise TypeError('文件/文件夹 {} 不存在或不合法！'.format(pathname))
    return _filename_list


def _is_legal_postfix(filename):
    return filename.split('.')[-1].lower() in _handle_postfix and not os.path.basename(filename).startswith('~')