

def find_ap(graph, d, l, vi, p, u, t):
	vi[u] = 1
	d[u] = t
	l[u] = d[u]
	for v in graph[u]:
		if vi[v] == 0:
			p[v] = u
			t += 1
			find_ap(graph, d, l, vi, p, u, t)
			l[u] = min(l[u], l[v])
			# handle articulation points
			if p[u] != -1 and d[u] <= l[v]:
				print u
			elif p[u] == -1 and child > 1:
				print u
		elif p[u] != v:
			l[u] = min(l[u], d[v])


