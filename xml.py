from xml.dom import minidom 
import traceback

def fun1():
    f = open("xmlstuff.xml", "w") 
     
    doc = minidom.Document() 
    rootNode = doc.createElement("root") 
    doc.appendChild(rootNode) 
    bookNode = doc.createElement("book") 
    bookNode.setAttribute("isbn", "34909023") 
    rootNode.appendChild(bookNode) 
    authorNode = doc.createElement("author") 
    bookNode.appendChild(authorNode) 
    authorTextNode = doc.createTextNode("dikatour") 
    authorNode.appendChild(authorTextNode) 
    doc.writexml(f, "\t", "\t", "\n", "utf-8") 
    f.close() 
def fun2():
    f2 = open("xmlstuff.xml", "r")
    strl= ""
    for line in f2.readlines():
        strl = strl + str(line).strip()
    f2.close()
    f2 = open("xmlstuff.xml", "w")
    f2.write(strl)
    f2.close()
    doc = minidom.parse("xmlstuff.xml")
    rootNode = doc.getElementsByTagName('root')[0]
    tmpDoc = minidom.Document().createElement('book')
    tmpDoc.setAttribute("isbn", "34909023")  
    authorNode = doc.createElement("author")
    authorTextNode = doc.createTextNode("dikatour")
    authorNode.appendChild(authorTextNode)
    tmpDoc.appendChild(authorNode)
    #rootNode.appendChild(tmpDoc)
    for node in rootNode.getElementsByTagName('book'):
        for node1 in node.getElementsByTagName('author'):
            if node1.hasChildNodes():
                node2 = node1.firstChild
                print node2.nodeType
                print node2.nodeType == node1.TEXT_NODE
                print node2.nodeValue

        #print node.isSameNode(tmpDoc)
    
    f = open("xmlstuff.xml", "w")
    doc.writexml(f, "\t", "\t", "\n", "utf-8") 
    f.close()     
'''
<web-app
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
        <welcome-file>index.htm</welcome-file>
        <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>
	
	<filter>
		<filter-name>CSRFFilter</filter-name>
		<filter-class>test</filter-class>
	</filter>
	<filter-mapping>
		<filter-name>CSRFFilter</filter-name>
		<url-pattern>/main/*</url-pattern>
	</filter-mapping>
'''
if __name__=="__main__":
    fun2()
    pass
