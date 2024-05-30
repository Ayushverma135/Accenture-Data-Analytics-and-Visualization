import pandas as pd

# Load the datasets
content = pd.read_csv('ContentCleaned.csv')
content=content.iloc[:,1:]
reaction = pd.read_csv('ReactionsCleaned.csv')
reaction=reaction.iloc[:,1:]
reaction_type = pd.read_csv('ReactionTypesCleaned.csv')
reaction_type=reaction_type.iloc[:,1:]

# Merge reaction and content datasets on 'Content ID'
merged_df = pd.merge(reaction, content, on='Content ID')

# Merge the above result with reaction_type on 'Reaction Type'
final_df = pd.merge(merged_df, reaction_type, on='Reaction Type')

# Calculate total score for each category
category_scores = final_df.groupby('Category')['Score'].sum().reset_index()

# Sort categories by total score in descending order and get top 5
top_5_categories = category_scores.sort_values(by='Score', ascending=False).head(5)

# Print the top 5 categories
print(top_5_categories)

# Save the final cleaned dataset and the top 5 categories to Excel files
final_df.to_excel('final_dataset.xlsx', index=False)
# final_df.to_csv('final_dataset.xlsx', index=False)
top_5_categories.to_excel('top_5_categories.xlsx', index=False)
# top_5_categories.to_csv('top_5_categories.xlsx', index=False)
