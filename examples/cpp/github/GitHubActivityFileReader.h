/*
 * CMSC 12300 - Computer Science with Applications 3
 * Borja Sotomayor, 2013
 *
 * Implementation of the USAGovClickReader abstract class
 * for click data stored in a text file.
 *
 */

#ifndef GITHUBACTIVITYFILEREADER_H_
#define GITHUBACTIVITYFILEREADER_H_

#include "GitHubActivityReader.h"
#include <iostream>

class GitHubActivityFileReader: public GitHubActivityReader {
	// Input stream.
	std::istream &is;

public:
	// Constructor
	// Parameter: The input stream with the event data.
	GitHubActivityFileReader(std::istream &is);

	// Destructor
	virtual ~GitHubActivityFileReader();

	// Implementation of GitHubActivityReader abstract methods.
	// See GitHubActivityReader.h for details.
	bool done();
	GitHubActivityEvent next();
};

#endif /* GITHUBACTIVITYFILEREADER_H_ */
