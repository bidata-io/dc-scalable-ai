# Initialize DataLoader
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_data = CIFAR10(root='data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Initialize the model and trainer
model = CNNModel()
trainer = pl.Trainer(max_epochs=10, logger=True, checkpoint_callback=True)

# Train the model
trainer.fit(model, train_loader)
