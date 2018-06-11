#ifndef GRAPH_H
#define GRAPH_H
#include <unordered_map>
#include <queue>
#include <functional>
#include <climits>

#include "Vertex.h"
using namespace std;
class Graph
{
	unordered_map<int, Vertex> _vertices;

public:

	void addVertex(Vertex vertex)
	{
		_vertices[vertex.getId()] = vertex;
	}

	//MA #12 TODO: IMPLEMENT!
	unordered_map<Vertex, int> computeShortestPath(Vertex *start)
	{

		//holds known distances
		unordered_map<Vertex, int> distances;
		unordered_map<Vertex, bool> known;
		// initiate distances to inf
        for (auto vertex : _vertices)
        {
            distances[vertex.second.getId()] = INT_MAX;
        }
		//underlying heap
		priority_queue<Vertex, vector<Vertex>, PathWeightComparer> dijkstra_queue{};
		//reset start's path weight
		start->setPathWeight(0);
		//make sure that the starting vertex is in the graph
		if (containsVertex(*start))
		{
			//push on starting vertex
            dijkstra_queue.push(_vertices[start->getId()]);
            distances[_vertices[start->getId()]] = 0;
            known[_vertices[start->getId()]] = true;
			//while queue not empty
			while (!dijkstra_queue.empty())
			{
                auto vert = dijkstra_queue.top();
                auto edges = vert.getEdges();

                dijkstra_queue.pop();
                for (auto ed : edges) // For each edge adjacent to the vertex
                {
                    if (vert.getEdgeWeight(ed.first) + vert.getPathWeight() < distances[ed.first->getId()]) // if this path is less than current distance logged
                    {
                        // update new path weight
                        _vertices[ed.first->getId()].setPathWeight(vert.getEdgeWeight(ed.first) + vert.getPathWeight());
                        // update new distance to vertice
                        distances[ed.first->getId()] = vert.getEdgeWeight(ed.first) + vert.getPathWeight();
                    }
                    // push vertice onto priority queue
                    if (known[_vertices[ed.first->getId()]] == false)
                    {
                    known[_vertices[ed.first->getId()]] = true;
                    dijkstra_queue.push(_vertices[ed.first->getId()]);
                    }
                }
				//Top of heap not known (in distances)?
					//make known
            }
					//push on outgoing edges
        }
		return distances;
	}

	bool containsVertex(Vertex vert)
	{
        bool contains = false;
        for (auto vertex : _vertices)
        {
            if (vertex.second == vert)
            {
                contains = true;
                break;
            }
        }
        return contains;
	}
};

#endif
