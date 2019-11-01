Output of rs.status()
```rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T21:39:20.875Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T21:40:56.330Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T21:40:56.330Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T21:40:56.330Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T21:40:56.330Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572422619, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572422619, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-11-01T19:41:14.150Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572378460, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T19:41:15.073Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T19:41:15.993Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "node0:27017",
			"ip" : "172.31.47.76",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 45173,
			"optime" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T21:40:40Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572378074, 1),
			"electionDate" : ISODate("2019-11-01T19:41:14Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "node1:27017",
			"ip" : "172.31.8.112",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 44878,
			"optime" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T19:41:14Z"),
			"optimeDurableDate" : ISODate("2019-11-01T19:41:14Z"),
			"lastHeartbeat" : ISODate("2019-11-01T19:42:36Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:41:17Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node1:27017",
			"syncSourceHost" : "node1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "node2:27017",
			"ip" : "172.31.24.79",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 44878,
			"optime" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T19:41:14Z"),
			"optimeDurableDate" : ISODate("2019-11-01T19:41:14Z"),
			"lastHeartbeat" : ISODate("2019-11-01T19:42:36Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:41:17Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node1:27017",
			"syncSourceHost" : "node1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572422639, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572422639, 1)
}
```

Output of rs.config() 
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "node0:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "node1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "node2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db575fa1719e051a2648054")
	}
}
```

Screenshot of application with most recent messages:

![alt text](https://github.com/charikova/distributed_systems/blob/master/lab9/Screen%20Shot%202019-11-01%20at%209.29.45%20PM.png)

Output of rs.status() after shutdown VPS with primary mongodb instance:
```
rs0:SECONDARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T21:39:20.875Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T21:40:56.330Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T21:40:56.330Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572422639, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T21:40:56.330Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T21:40:56.330Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572422619, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572422619, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-11-01T19:41:14.150Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572378460, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
    "priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T19:41:15.073Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T19:41:15.993Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "node0:27017",
			"ip" : "172.31.47.76",
			"health" : 1,
			"state" : 1,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 45173,
			"optime" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
        "ts" : Timestamp(0, 0),
        "t" : NumberLong(-1)
        },
      "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
      "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
      "lastHeartbeat" : ISODate("2019-11-01T20:19:28.464Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T20:18:27.658Z"),
      "pingMs" : NumberLong(1),
      "lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
      "syncingTo" : 1"",
		},
		{
			"_id" : 1,
			"name" : "node1:27017",
			"ip" : "172.31.8.112",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 44878,
			"optime" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T19:41:14Z"),
			"optimeDurableDate" : ISODate("2019-11-01T19:41:14Z"),
			"lastHeartbeat" : ISODate("2019-11-01T19:42:36Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:41:17Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node1:27017",
			"syncSourceHost" : "node1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "node2:27017",
			"ip" : "172.31.24.79",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 44878,
			"optime" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572422639, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T19:41:14Z"),
			"optimeDurableDate" : ISODate("2019-11-01T19:41:14Z"),
			"lastHeartbeat" : ISODate("2019-11-01T19:42:36Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T19:41:17Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node1:27017",
			"syncSourceHost" : "node1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572422639, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(1)
		}
	},
	"operationTime" : Timestamp(1572422639, 1)
}
```
Output of rs.config() after shutdown VPS with primary mongodb instance:
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "node0:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "node1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "node2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db575fa1719e051a2648054")
	}
}
```
Screenshot of application with most recent messages after shutdown VPS with primary mongodb instance:


![alt text](https://github.com/charikova/distributed_systems/blob/master/lab9/Screen%20Shot%202019-11-01%20at%210.20.11%20PM.png)
