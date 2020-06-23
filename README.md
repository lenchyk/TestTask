# TestTask
Locating an element on web pages with some differences.

Used Python Selenium packet for automation. So it took me a while for installing it along with necessary servers (chromedriver).

Analyzing html source code I found out that good button had its own class name (the same) - 'btn btn-success'.
So I thought it would be better to locate the element (this green button) with its class name rather than its id, for other sites didn't contain that info.

Still I didn't get Xpath from this button (couldn't find out how exactly it's generated). Also didn't tested it properly for different variations that were provided.
