import coremltools

input_features = ["symptoms"]
output_feature = "medical condition"
model = coremltools.converters.keras.convert('my_model.h5',input_features,output_feature)
print("successfully loaded keras model")

model.save('HeightWeight_model.mlmodel')
#coremltools.utils.save_spec(coreml_model, 'my_model.mlmodel')
print("successfully saved coreML model")