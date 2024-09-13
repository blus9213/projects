#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Node {
public:
    string name;
    vector<Node*> children;

    Node(string name) : name(name) {}

    void add_child(Node* child) {
        children.push_back(child);
    }
};

class Tree {
public:
    Node* root;

    Tree() {
        root = new Node("root");
    }

    void construct_tree(vector<pair<string, string>>& routes) {
        for (auto& route : routes) {
            Node* current = root;
            string start = route.first;
            string end = route.second;

            size_t pos = 0;
            while ((pos = start.find('/')) != string::npos) {
                string node = start.substr(0, pos);
                start.erase(0, pos + 1);

                bool found = false;
                for (Node* child : current->children) {
                    if (child->name == node) {
                        current = child;
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    Node* new_node = new Node(node);
                    current->add_child(new_node);
                    current = new_node;
                }
            }

            Node* new_node = new Node(end);
            current->add_child(new_node);
        }
    }

    void pre_order_traversal(Node* node) {
        cout << node->name << endl;
        for (Node* child : node->children) {
            pre_order_traversal(child);
        }
    }

    bool bfs(Node* node, string target) {
        queue<Node*> q;
        q.push(node);

        while (!q.empty()) {
            Node* current = q.front();
            q.pop();
            if (current->name == target) {
                return true;
            }
            for (Node* child : current->children) {
                q.push(child);
            }
        }
        return false;
    }

    bool dfs(Node* node, string target) {
        if (node->name == target) {
            return true;
        }
        for (Node* child : node->children) {
            if (dfs(child, target)) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    vector<pair<string, string>> routes = {
        {"USA/NYC", "Canada/Toronto"},
        {"USA/NYC", "Mexico/Cancun"},
        {"Canada/Toronto", "USA/Chicago"},
        {"Canada/Toronto", "UK/London"},
        {"Mexico/Cancun", "USA/Miami"},
        {"UK/London", "France/Paris"}
    };

    Tree tree;
    tree.construct_tree(routes);
    tree.pre_order_traversal(tree.root);

    cout << "BFS:" << endl;
    cout << boolalpha << tree.bfs(tree.root, "France/Paris") << endl; // True
    cout << boolalpha << tree.bfs(tree.root, "Germany/Berlin") << endl; // False

    cout << "DFS:" << endl;
    cout << boolalpha << tree.dfs(tree.root, "France/Paris") << endl; // True
    cout << boolalpha << tree.dfs(tree.root, "Germany/Berlin") << endl; // False

        return 0;
}
