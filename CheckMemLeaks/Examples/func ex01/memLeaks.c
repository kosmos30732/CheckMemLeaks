struct node { int key; node* lt; node* rt; };
void ex01(node* p, int v) {
	node* x, * y;
	if (v < p->key)
		x = p->lt;
	else
		x = p->rt;
	if (v < x->key) {
		y = x->lt;
		x->lt = y->rt;
		y->rt = x;}
	else {
		y = x->rt;
		p->lt = x->rt
		x = malloc();}
	if (v >= p->key)
		p->lt = x;
	else
		p->rt = x;
}