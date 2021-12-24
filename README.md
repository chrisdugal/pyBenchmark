# pyBenchmark

- `pip install -r requirements.txt`

- requires `.env` file with following keys:

```
CHROMEDRIVER_PATH
USERNAME
PASSWORD
```

## TODO

- make config.json file with number of games for each benchmark test
- refactor so setup/login gets run, then have a file/function for each test that gets run in a loop the desired number of times
