def test_solution():
    try:
        # Check if the model has the correct layers
        model = CNNModel()
        assert isinstance(model.conv1, nn.Conv2d) and model.conv1.out_channels == 16, "conv1 is incorrect"
        assert isinstance(model.conv2, nn.Conv2d) and model.conv2.out_channels == 32, "conv2 is incorrect"
        assert isinstance(model.fc1, nn.Linear) and model.fc1.out_features == 128, "fc1 is incorrect"
        assert isinstance(model.fc2, nn.Linear) and model.fc2.out_features == 10, "fc2 is incorrect"
        
        # Check if the Trainer is correctly initialized
        trainer = pl.Trainer(max_epochs=10, logger=True, checkpoint_callback=True)
        assert trainer.max_epochs == 10, "Trainer max_epochs is incorrect"
        
        # Test model training with a small dataset
        transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
        train_data = CIFAR10(root='data', train=True, download=True, transform=transform)
        train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
        trainer.fit(model, train_loader)
        success_message = "Congratulations! Your model is correctly implemented and successfully trained."
        print(success_message)
    except AssertionError as e:
        print("Test failed:", str(e))
    except Exception as e:
        print("Solution failed during training:", str(e))

# Run the test
test_solution()
