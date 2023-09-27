import React, { useState, Component } from 'react';


class ImageUploader extends Component {
    constructor(props) {
      super(props);
      this.state = {
        selectedImage: null,
      };
    }

    handleImageChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                this.setState({
                  selectedImage: e.target.result,
                });
                // Send the image data to the Python server
                this.sendImageDataToPython(file);
              };
              reader.readAsDataURL(file);
        }
    }

    //incorrect, must redo eventually
    sendImageDataToPython = (imageData) => {
      const formData = new FormData();
      formData.append('file', imageData);
      fetch('http://127.0.0.1:5000/',{ 
        method: "POST",
        headers: {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*',
        },
        mode: 'no-cors',
        body: formData

      })
    
        .then((response) => {
          console.log(response.data); // Do something with the response from Python
        })
        .catch((error) => {
          console.error(error);
        });
    };

    render() {
        const { selectedImage } = this.state;
    
        return (
          <div>
            <input
              type="file"
              accept="image/*"
              onChange={this.handleImageChange}
            />
            {selectedImage && (
              <div>
                <img src={selectedImage} alt="Uploaded" />
              </div>
            )}
          </div>
        );
      }
    }

export default ImageUploader;



