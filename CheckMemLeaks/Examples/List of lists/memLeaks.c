typedef struct List
{
    int key;
    struct List* next;
} List;
typedef struct Node
{
    int value;
    struct Node* next;
    struct List* keyList;
} Node;
void insert_back(int value, int key, Node* node)
{
    List* el, * tmp;
    el = malloc(sizeof(List));
    node = node->next;
    el->key = key;
    if (node->value > value)
    {
        Node* newNode;
        newNode = malloc(sizeof(Node));
        newNode->keyList = el;
        node->next = newNode;
    }
    else
    {
        tmp = node->keyList;
        node->keyList = el;
        el->next = tmp;
    }
}