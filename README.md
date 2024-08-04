# TarotAI

made by brAIns

## How to use:

1. Clone the repository.

```shell
git clone https://github.com/dirac042/TarotAI.git
```

2. install all the requirements.

   1. using makefile

   ```shell
   make install
   ```

   2. using install.sh

   ```shell
   chmod +x install.sh
   ./install.sh
   ```
3. Write `secret.py` with following contents:
```python
sender_email = <YOUR_EMAIL_ADDRESS>
password = <YOUR_EMAIL_PASSWORD>
```

4. Fill in `my_api_key` with your own OpenAI api key.

5. run 'main.py' via Shell.

```shell
python3 main.py
```
