
# Payload for Tryhackme Hammer 

Payload to bruteforce the OTP for the Hammer Room found here: https://tryhackme.com/room/hammer

It will mainly bruteforce the OTP an then you must copy the PHPSESSION 






## Deployment

Change the ip variable in the code with the ip given by the room
```python
  ip="X.X.X.X"
```
then

```python
  python3 index.py
```


## Lessons Learned

- Payload creation
- BurpSuite request breakdown
- JWT vulnerabilities made by the developer
- the tool fuff to fuzz http url requests and the body of the request

