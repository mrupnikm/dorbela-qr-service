
# DoorBella QR

A simple Python API template using Flask that can be used as a QR doorbell service. This project can be build in docker by exposing port 5000 from the container.

The way it works is that it generates a QR code on start and stores it localy. The QR code can be accessed by calling `/home` on the API. 
Printing the QR code and placing it in the desired location provides a way for anybody to trigger a notification to your desired location over any API.


## Importaint!
- There is currently no written notification service as this is meant to be a template project, but there is an option to add it in `dorbella` function to connect and notify.
- Currently there is no extra security in place.
