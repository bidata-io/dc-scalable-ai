import torchmetrics

# Assume 'model' is your trained model and 'test_loader' is your DataLoader for the test dataset
# Evaluate model on test dataset
model.eval()
accuracy_metric = torchmetrics.Accuracy()
all_preds = []
all_labels = []

for inputs, labels in test_loader:
    outputs = model(inputs)
    preds = torch.argmax(outputs, dim=1)
    all_preds.append(preds)
    all_labels.append(labels)

# Calculate accuracy
accuracy = accuracy_metric(torch.cat(all_preds), torch.cat(all_labels))

# Print accuracy
print(f"Model accuracy: {accuracy:.2f}")
