const selectDoctor = document.querySelectorAll("h2.click");

selectDoctor.forEach(function (h2) {
    h2.addEventListener("click", function () {
        let selectedDiv = document.querySelector(".selectedCard");
        selectedDiv.style.display = "inline-block";
        selectedDiv.style.float = "right";

    });
});


// code for the search input and fetch data from the backend(Python) with database(MariaDB)

document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.querySelector('#searchForm');
    const typeInput = document.querySelector('#typeSelect');
    const cityInput = document.querySelector('#citySelect');
    const expertInput = document.querySelector('#expertSelect');
    const searchBtn = document.querySelector('#searchButton');
    const searchResults = document.querySelector('#searchResults');
    const textField = document.querySelector('#textField');

    if (!searchForm || !typeInput || !cityInput || !expertInput || !searchBtn || !searchResults) {
        console.error('One or more required elements were not found in the document.');
        return;
    }

    // New function to fetch at least first 3 data
    function performSearch(e) {
        e.preventDefault();

        // Get input values
        const typeValue = typeInput.value.trim();
        const cityValue = cityInput.value.trim();
        const expertValue = expertInput.value.trim();

        // Validate inputs
        if (!typeValue || !cityValue || !expertValue) {
            textField.innerHTML = '<p>Please provide type, city, and expertise.</p>';
            return;
        }

        // Prepare request payload
        const requestData = {
            type: typeValue,
            city: cityValue,
            expert: expertValue,
        };

        // Send POST request to the backend
        fetch('/search_input', {
            method: 'POST',
            body: JSON.stringify(requestData),
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                if (!response.ok) {
                    console.error(`Network response was not ok: ${response.status} ${response.statusText}`);
                    textField.innerHTML = '<p>There was an error fetching the data. Please try again later.</p>';
                    return;
                }
                return response.json();  // Parse JSON response
            })
            .then(data => {
                if (!data) {
                    textField.innerHTML = '<p>There was an error processing the response.</p>';
                    return;
                }

                // Clear previous search results
                searchResults.innerHTML = '';
                textField.innerHTML = '';

                // Display search results
                textField.innerHTML = `<p>Search results for: (Type): <strong>${typeValue}</strong> in (City): <strong>${cityValue}</strong> with (Expertise): <strong>${expertValue}</strong></p>`;

                // Function to populate the cards on the left side
                function populateCards(data) {
                    // Identify the card elements
                    const doctorCards = document.querySelectorAll('.doctor.card');
                    const facilityCard = document.querySelector('.facility.card');

                    // Populate doctor cards
                    if (data.Doctors && data.Doctors.length > 0) {
                        for (let idx = 0; idx < doctorCards.length; idx++) {
                            if (idx >= data.Doctors.length) {
                                break; // Stop if there are no more doctors to display
                            }

                            const doctor = data.Doctors[idx];
                            const card = doctorCards[idx];

                            // Populate card with doctor information
                            card.querySelector('.nameElem').textContent = doctor.Name;
                            // card.querySelector('.hospName').textContent = doctor.Company;
                            card.querySelector('.hospInfo').innerHTML = `
                                <p>Expertise: ${doctor.Expertise}</p>
                                <p>Hospital: ${doctor.Company}</p>
                            `;

                            // Blurb => is a kiwi thing and a short description of a book, movie, or other product written for promotional purposes 
                            // and appearing on the cover of a book or in an advertisement.

                            card.querySelector('.blurb').textContent = `This is the official information of '${doctor.Name}'. Please click the card for additional inquiry!`;
                        }
                    }

                    // Populate facility card
                    if (data.Facilities && data.Facilities.length > 0 && facilityCard) {
                        const facility = data.Facilities[0]; // Take the first info in the Facility data
                        // Populate card with facility information
                        facilityCard.querySelector('.nameElem').textContent = facility.Name;
                        facilityCard.querySelector('.hospAddress').textContent = `Address: ${facility.Address} `;
                        facilityCard.querySelector('.hospPhone').textContent = `Phone: ${facility.Phone} `;
                        facilityCard.querySelector('.blurb').textContent = `This the official data of the '${facility.Name}'. Please select the card for more additional information`;
                    }
                }

                // After receiving the response data from the server
                // Call the function to populate cards
                populateCards(data);


                //Add event listener for the cards on the left and when click it will populate the data on the card on right side (.selectedCard)



                // We do not need this code, we keep it only because the code might not work
                // Display doctor results (first 3)
                if (data.Doctors && data.Doctors.length > 0) {
                    const doctorsSection = document.createElement('div');
                    doctorsSection.innerHTML = '<h3>Doctors:</h3>';

                    // Display up to 3 doctors
                    let doctorCount = 0;
                    for (const doctor of data.Doctors) {
                        if (doctorCount >= 3) break;
                        const doctorDiv = document.createElement('div');
                        doctorDiv.innerHTML = `
                            Name: ${doctor.Name},
                            Expertise: ${doctor.Expertise},
                            Company: ${doctor.Company},
                            Address: ${doctor.Address},
                            Phone: ${doctor.Phone}
                            `;
                        doctorDiv.style.margin = '1.5rem';
                        doctorsSection.appendChild(doctorDiv);
                        doctorCount++;
                    }

                    searchResults.appendChild(doctorsSection);
                } else {
                    searchResults.innerHTML += '<p>No doctors found matching your criteria.</p>';
                }

                // Display facilities results (first 3)
                if (data.Facilities && data.Facilities.length > 0) {
                    const facilitiesSection = document.createElement('div');
                    facilitiesSection.innerHTML = '<h3>Facilities:</h3>';

                    // Display up to 3 facilities
                    let facilityCount = 0;
                    for (const facility of data.Facilities) {
                        if (facilityCount >= 3) break;
                        const facilityDiv = document.createElement('div');
                        facilityDiv.innerHTML = `
                            Name: ${facility.Name},
                            Type: ${facility.Type},
                            Address: ${facility.Address},
                            Phone: ${facility.Phone},
                            Emergency: ${facility.Emergency},
                            Services: ${facility.Services}
                            `;
                        facilityDiv.style.margin = '1.5rem';
                        facilitiesSection.appendChild(facilityDiv);
                        facilityCount++;
                    }
                    searchResults.appendChild(facilitiesSection);
                } else {
                    searchResults.innerHTML += '<p>No facilities found matching your criteria.</p>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                textField.innerHTML = '<p>There was an error fetching the data. Please try again later.</p>';
            });
    }

    // Add event listener to the search button
    searchBtn.addEventListener('click', performSearch);

    // Add event listener to the form submission
    searchForm.addEventListener('submit', performSearch);
});


// Old function to fetch all data -> Goes inside the DOMContentLoaded

// // Function to handle the search action
// function performSearch(e) {
//     e.preventDefault();

//     // Get input values
//     const typeValue = typeInput.value.trim();
//     const cityValue = cityInput.value.trim();
//     const expertValue = expertInput.value.trim();

//     // Validate inputs
//     if (!typeValue || !cityValue || !expertValue) {
//         // searchResults.innerHTML = '<p>Please provide type, city, and expertise.</p>';
//         textField.innerHTML = '<p>Please provide type, city, and expertise.</p>';
//         return;
//     }

//     // Prepare request payload
//     const requestData = {
//         type: typeValue,
//         city: cityValue,
//         expert: expertValue,
//     };

//     // Send POST request to the backend
//     fetch('/search_input', {
//         method: 'POST',
//         body: JSON.stringify(requestData),
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     })
//         .then(response => {
//             if (!response.ok) {
//                 console.error(`Network response was not ok: ${ response.status } ${ response.statusText } `);
//                 // searchResults.innerHTML = '<p>There was an error fetching the data. Please try again later.</p>';
//                 textField.innerHTML = '<p>There was an error fetching the data. Please try again later.</p>';
//                 return;
//             }
//             return response.json();  // Parse JSON response
//         })
//         .then(data => {
//             if (!data) {
//                 // searchResults.innerHTML = '<p>There was an error processing the response.</p>';
//                 textField.innerHTML = '<p>There was an error processing the response.</p>';
//                 return;
//             }

//             // Clear previous search results
//             searchResults.innerHTML = '';
//             textField.innerHTML = '';

//             // Display search results
//             // searchResults.innerHTML += `< p > Search results for: type: <strong>${typeValue}</strong> in city: <strong>${cityValue}</strong> with expertise: <strong>${expertValue}</strong></ > `;
//             textField.innerHTML = `< p > Search results for: (Type): <strong>${typeValue}</strong> in (City): <strong>${cityValue}</strong> with (Expertise): <strong>${expertValue}</strong></ > `;

//             // Display doctor results
//             if (data.Doctors && data.Doctors.length > 0) {
//                 const doctorsSection = document.createElement('div');
//                 doctorsSection.innerHTML = '<h3>Doctors:</h3>';
//                 data.Doctors.forEach(doctor => {
//                     const doctorDiv = document.createElement('div');
//                     doctorDiv.innerHTML = `
//                     Name: ${doctor.Name},
//                     Expertise: ${doctor.Expertise},
//                     Company: ${doctor.Company},
//                     Address: ${doctor.Address},
//                     Phone: ${doctor.Phone}
//                 `;
//                     doctorDiv.style.margin = '1.5rem';
//                     doctorsSection.appendChild(doctorDiv);
//                 });
//                 searchResults.appendChild(doctorsSection);
//             } else {
//                 searchResults.innerHTML += '<p>No doctors found matching your criteria.</p>';
//             }

//             // Display facilities results
//             if (data.Facilities && data.Facilities.length > 0) {
//                 const facilitiesSection = document.createElement('div');
//                 facilitiesSection.innerHTML = '<h3>Facilities:</h3>';
//                 data.Facilities.forEach(facility => {
//                     const facilityDiv = document.createElement('div');
//                     facilityDiv.innerHTML = `
//                     Name: ${facility.Name},
//                     Type: ${facility.Type},
//                     Address: ${facility.Address},
//                     Phone: ${facility.Phone},
//                     Emergency: ${facility.Emergency},
//                     Services: ${facility.Services}
//                 `;
//                     facilityDiv.style.margin = '1.5rem';
//                     facilitiesSection.appendChild(facilityDiv);
//                 });
//                 searchResults.appendChild(facilitiesSection);
//             } else {
//                 searchResults.innerHTML += '<p>No facilities found matching your criteria.</p>';
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             // searchResults.innerHTML = '<p>There was an error fetching the data. Please try again later.</p>';
//             textField.innerHTML = '<p>There was an error fetching the data. Please try again later.</p>';
//         });
// }

// // Add event listener to the search button
// searchBtn.addEventListener('click', performSearch);

// // Add event listener to the form submission
// searchForm.addEventListener('submit', performSearch);