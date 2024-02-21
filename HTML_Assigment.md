# HTTP/2 VS HTTP/3

## Problem with HTTP2
- There are head-of-lying blocking issues at the TCP level
  - Network congestion results in packet loss.
  - This interruption in the TCP connection blocks all streams despite the packet loss only concerning one request.

## How HTTP/3 fixes this problem
- HTTP/3 makes use of the QUIC transport protocol
  - Makes use of UDP protocol to establish faster connections
  - Transport logic was implemented which means that packet loss can be dealt with
    - Without blocking all streams, the correct packet can be requested once again and delivered to the correct stream.
  - Requests and responses are multiplexed over independent streams which prevents head-of-lying blocking at HTTP and TCP levels
  - This ultimately means that data can continue to be transferred while lost packets are being resolved

## QUIC
- Despite being on a UDP protocol it is still secure
  - 
