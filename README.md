# aes_crypto_python

это реализация библиотеки [crypto](https://github.com/chrisveness/crypto) на языке Python

## пример использования

```python
from aes import aes

text = "Lorem Ipsum is simply dummy text of the printing and ..."
key = "password"
entext = aes.Aes.Ctr.encrypt(text, key, 256)
print(entext)
print(aes.Aes.Ctr.decrypt(entext, key, 256))
```