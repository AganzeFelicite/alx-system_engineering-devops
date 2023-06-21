POSTMORTEM
![Animated GIF](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)
Issues Summary
---------------
From 6.25 AM to 9.54 AM EAT, requests sent to the website House_Hunting resulted in a 500 error response message. This resulted in most users, typically 90%, experiencing slow service while trying to access our website due to a root cause of traffic overload because of poor configuration of the website infrastructure. Timeline (all times East Africa Time)
Time line
----------
9.58 AM: Lots of emails received about slow service
10.00 AM: Outage begins looking for faults
10.20 AM: On-site engineer tests website and confirms and escalates to the on-call engineer
10.30 AMM: Debugging begins until the error found is due to overload IN The Request made to the server
11.50 AM: Round-robin load balancing set up
10:40 AM: Server restarted by the on call engineer
10:40 AM: 100% traffic now accesses the website quickly

Root Cause
-----------
At 9.54 PM EAT, our team was alerted of slow traffic to our website which we established later was due to an overload of traffic to our website during the first Black Friday day of November. The single server was overworked because it was incapable of fulfilling all those requests at that particular point in a timely manner. Traffic was then queued and later became unavailable until an outage at 10.40 AM EAT.

Resolution
-----------
After the problem was established, our engineers employed a load balancing technique, using the round-robin technique to distribute traffic across three servers, after the addition and configuration of two more Nginx servers to prevent a single point of failure. The client requests are now distributed in turn across the different servers to prevent overload.

Corrective and Preventative Measures
-------------------------------------
More actions will be taken during the next couple of days to ensure faster delivery and low latency times while trying to access our website. We’ve also removed a single point of failure with new servers but configured them to reduce redundancy. Some of what we plan to do include:

Deploy NGINX PLUS that uses the round-robin technique but can be configured to use weighted or dynamic round-robin algorithms.
We plan on adopting a hybrid model with some of the systems running on-site while others on the cloud provider, AWS by Amazon.
We will set up SolarWinds Server and Application Monitor (SAM) as our choice of monitoring tool that will monitor our on-prem and cloud infrastructure, when the system needs attention, we’ve configured it to send emails and text messages to our principal engineers before total shutdown.