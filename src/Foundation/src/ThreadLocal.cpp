//
// ThreadLocal.cpp
//
// Library: Foundation
// Package: Threading
// Module:  Thread
//
// Copyright (c) 2004-2006, Applied Informatics Software Engineering GmbH.
// and Contributors.
//
// SPDX-License-Identifier:	BSL-1.0
//


#include "Poco/ThreadLocal.h"
#include "Poco/Thread.h"


namespace Poco {


TLSAbstractSlot::TLSAbstractSlot()
{
}


TLSAbstractSlot::~TLSAbstractSlot()
{
}


ThreadLocalStorage::ThreadLocalStorage()
{
}


ThreadLocalStorage::~ThreadLocalStorage()
{
	for (auto& p: _map)
	{
		delete p.second;
	}
}


TLSAbstractSlot*& ThreadLocalStorage::get(const void* key)
{
	TLSMap::iterator it = _map.find(key);
	if (it == _map.end())
		return _map.insert(TLSMap::value_type(key, reinterpret_cast<Poco::TLSAbstractSlot*>(0))).first->second;
	else
		return it->second;
}


ThreadLocalStorage& ThreadLocalStorage::current()
{
	Thread* pThread = Thread::current();
	if (pThread)
	{
		return pThread->tls();
	}
	else
	{
		static ThreadLocalStorage tls;
		return tls;
	}
}


void ThreadLocalStorage::clear()
{
	Thread* pThread = Thread::current();
	if (pThread)
		pThread->clearTLS();
}


} // namespace Poco
