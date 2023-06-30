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
		x->rt = y->lt;
		y = malloc();}
	if (v >= p->key)
		p->lt = y;
	else
		p->rt = y;
}
