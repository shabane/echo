"""some tools are writed here
"""    


def re_wrapp_domain(key: str, domain: str, port: int):
    pre_domain = key[key.find('@')+1:key.find('/?')]
    return key.replace(pre_domain, f'{domain}:{port}')
