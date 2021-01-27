from distutils.core import setup
setup(
  name = 'ltspice2svg',
  packages = ['ltspice2svg'],
  version = '2021.01',
  license='MIT',
  description = 'Converting LTspice file to SVG',
  author = 'Harsh Agarwal',
  author_email = 'harshvinay752@gmail.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['LTspice','spice','SVG','vector','image','convert'],
  install_requires=['svgwrite'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: End-Users',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
