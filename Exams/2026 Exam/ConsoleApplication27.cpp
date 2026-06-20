#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

struct AnswerRecord
{
	string question;
	string team;
	double time;
};

struct TeamStatistics
{
	string team;
	double totalTime;
	int answerCount;
};

void readRecords(int& recordCount, AnswerRecord records[]);
void findQuestionsWithLongestAnswerTime(int recordCount, AnswerRecord records[], string questions[], double & time, int& questionCount);
void getUniqueTeams(int recordCount, AnswerRecord records[], string teams[], int& teamCount);
TeamStatistics calculateTeamStatistics(int recordCount, AnswerRecord records[], string teamName);
void sortTeamsByAnsCountDescendingThenByTimeAscending(TeamStatistics teamStats[], int teamCount);

int main()
{
	int teamCount;
	string teamNames[30];
	int recordCount;
	AnswerRecord records[15 * 30];
	int questionCount;
	double longestTime;
	string questions[15];
	TeamStatistics teamStats[30];


	readRecords(recordCount, records);
	findQuestionsWithLongestAnswerTime(recordCount, records, questions, longestTime, questionCount);
	getUniqueTeams(recordCount, records, teamNames, teamCount);

	for (int i = 0; i < teamCount; i++)
	{
		teamStats[i] = calculateTeamStatistics(recordCount, records, teamNames[i]);
	}

	sortTeamsByAnsCountDescendingThenByTimeAscending(teamStats, teamCount);

	ofstream fout("Rezultatai.txt");

	fout << longestTime << endl;
	
	for (int i = 0; i < questionCount; i++)
	{
		if (i > 0)
			fout << " ";
		fout << questions[i];
	}
	fout << endl;

	for (int i = 0; i < teamCount; i++)
	{
		fout << teamStats[i].team << " ";
		fout << teamStats[i].answerCount << " ";
		fout << fixed << setprecision(1) << teamStats[i].totalTime << endl;
	}

	fout.close();

}

void readRecords(int & recordCount, AnswerRecord records[])
{
	int questionCount, teamCount;
	string question;

	ifstream fin("Duomenys.txt");

	recordCount = 0;
	fin >> questionCount;
	for (int i = 0; i < questionCount; i++)
	{
		fin >> question;
		fin >> teamCount;
		for (int j = 0; j < teamCount; j++)
		{
			fin >> records[recordCount].team >> records[recordCount].time;
			records[recordCount].question = question;
			recordCount++;
		}
	}

	fin.close();
}

void findQuestionsWithLongestAnswerTime(int recordCount, AnswerRecord records[], string questions[], double & time, int& questionCount)
{
	time = 0;
	questionCount = 0;

	for (int i = 0; i < recordCount; i++)
	{
		if (records[i].time > time)
		{
			time = records[i].time;
			questionCount = 1;
			questions[0] = records[i].question;
		}
		else if (records[i].time == time)
		{
			bool found = false;
			for (int j = 0; j < questionCount; j++)
			{
				if (questions[j] == records[i].question)
				{
					found = true;
					break;
				}
			}
			if (!found)
			{
				questions[questionCount] = records[i].question;
				questionCount++;
			}
		}
	}
}

void getUniqueTeams(int recordCount, AnswerRecord records[], string teams[], int& teamCount)
{
	teamCount = 0;
	for (int i = 0; i < recordCount; i++)
	{
		bool found = false;
		for (int j = 0; j < teamCount; j++)
		{
			if (teams[j] == records[i].team)
			{
				found = true;
				break;
			}
		}
		if (!found)
		{
			teams[teamCount] = records[i].team;
			teamCount++;
		}
	}
}

TeamStatistics calculateTeamStatistics(int recordCount, AnswerRecord records[], string teamName)
{
	TeamStatistics stats;
	stats.team = teamName;
	stats.totalTime = 0;
	stats.answerCount = 0;

	for (int i = 0; i < recordCount; i++)
	{
		if (records[i].team == teamName)
		{
			stats.totalTime += records[i].time;
			stats.answerCount++;
		}
	}

	return stats;
}

void sortTeamsByAnsCountDescendingThenByTimeAscending(TeamStatistics teamStats[], int teamCount)
{
	for (int i = 0; i < teamCount - 1; i++)
	{
		for (int j = 0; j < teamCount - i - 1; j++)
		{
			if (teamStats[j].answerCount < teamStats[j + 1].answerCount ||
				(teamStats[j].answerCount == teamStats[j + 1].answerCount && teamStats[j].totalTime > teamStats[j + 1].totalTime))
			{
				swap(teamStats[j], teamStats[j + 1]);
			}
		}
	}
}