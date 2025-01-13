void dfs(TreeNode* node, vector<int>& leaves){
  if (node == NULL) return;
  if (node->left == NULL && node->right == NULL){
    leaves.push_back(node->val);
  }
  dfs(node->left, leaves);
  dfs(node->right, leaves);
}
