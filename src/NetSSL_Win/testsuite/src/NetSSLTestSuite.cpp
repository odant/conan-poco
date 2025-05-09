//
// NetSSLTestSuite.cpp
//
// Copyright (c) 2006-2014, Applied Informatics Software Engineering GmbH.
// and Contributors.
//
// SPDX-License-Identifier:	BSL-1.0
//


#include "NetSSLTestSuite.h"
#include "SecureStreamSocketTestSuite.h"
#include "HTTPSClientTestSuite.h"
#include "TCPServerTestSuite.h"
#include "HTTPSServerTestSuite.h"
#include "WebSocketTestSuite.h"


CppUnit::Test* NetSSLTestSuite::suite()
{
	CppUnit::TestSuite* pSuite = new CppUnit::TestSuite("NetSSLTestSuite");

	pSuite->addTest(SecureStreamSocketTestSuite::suite());
	pSuite->addTest(HTTPSClientTestSuite::suite());
	pSuite->addTest(TCPServerTestSuite::suite());
	pSuite->addTest(HTTPSServerTestSuite::suite());
	pSuite->addTest(WebSocketTestSuite::suite());

	return pSuite;
}
