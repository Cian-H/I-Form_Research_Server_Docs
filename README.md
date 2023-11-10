

## 

## Welcome
Welcome to the documentation for the I-Form Research Server. This documentation is intended as a user guide for researchers who wish to use, maintain, and otherwise interact with the server. Currently, the server is still undergoing deployment and testing, and as such, this documentation is a work in progress. If you have any questions, please contact the server administrator<a href="#footnote-1"><sup>1</sup></a>.

<br>

## Overview
The I-Form Research Server is intended to provide an adaptable, scalable, and secure platform from which to host research applications, tools, and services. The server architecture provides an extremely stable core operating system, with a flexible and adaptable containerised application layer. This makes it possible to quickly and easily add new software to our own cloud system without the need to worry about the various complexities of configuring and maintaining a server for each application. Research software often has very specific, unique requirements and must be updated or replaced frequently. For a traditional server, this can be a significant challenge. By providing a flexible, stable foundation that avoids this problem, this system should allow researchers to focus on their research, rather than maintaining research infrastructure.

<br>

## Technical Details
The I-Form Research Server is constructed as an  on top of a minimal [OpenSUSE Leap Micro](https://get.opensuse.org/leapmicro/5.5/) operating system. This provides a stable, immutable core operating system that is designed to be extremely secure and stable. On top of this, we use [Docker](https://www.docker.com) to provide a containerised application layer. The combination of these tools allows us to build a server using almost any hardware that may be available, linking them together into a compute cluster. This allows us to scale the server as needed, adding more compute power as required.

<br><br>

## Footnotes
<p id="footnote-1">[1]: email the <a href="mailto:cian.hughes@dcu.ie">server administrator</a></p>