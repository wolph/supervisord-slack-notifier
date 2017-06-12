import setuptools
from slack_notifier.version import Version


setuptools.setup(
    name='slack_notifier',
    version=Version('1.0.0').number,
    description='Supervisord Slack Notifier',
    long_description=open('README.rst').read().strip(),
    author='Rick van Hattem',
    author_email='Wolph@wol.ph',
    url='https://github.com/WoLpH/supervisord-slack-notifier',
    py_modules=['slack_notifier'],
    install_requires=[
        'supervisor',
        'pyslack-real==0.5.3',
    ],
    tests_require=[
        'pytest==2.7.1',
        'pytest-cov==1.8.1',
    ],
    license='MIT License',
    zip_safe=False,
    keywords='supervisord slack listener notifications',
    packages=['slack_notifier'],
    entry_points=dict(
        console_scripts=[
            'slack_notifier = slack_notifier.slack_notifier:main',
        ],
    ),
)
