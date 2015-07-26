from setuptools import setup

setup(name='scwsutil',
      version='0.1',
      url='https://github.com/linhaobuaa/scwsutil/',
      author='linhaobuaa',
      packages=['scwsutil'],
      data_files=[('dict', ['dict/userdic.txt', 'dict/stopword.txt', 'dict/emotionlist.txt', 'dict/one_word_white_list.txt'])],
      install_requires=[
          'pyscws',
      ],
      dependency_links=[
      ],
)
