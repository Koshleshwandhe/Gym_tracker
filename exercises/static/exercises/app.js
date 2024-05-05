$(document).ready(function() {
    // Hide exercise table initially
    $('#exercise-table').hide();

    // Submit exercise form
    $('#exercise-form').submit(function(event) {
        event.preventDefault();

        // Collect form data
        const formData = $(this).serialize();

        // Send POST request to store exercise data
        $.ajax({
            url: '/exercises/', // Update the URL to match your Django view
            method: 'POST',
            data: formData,
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Include CSRF token
            },
            success: function(response) {
                // Hide form
                $('#exercise-form').hide();
                
                // Show exercise table
                $('#exercise-table').show();

                // Fetch and update exercise data after successful submission
                fetchExercises();
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });

    // Function to fetch exercise data from API
    function fetchExercises() {
        $.ajax({
            url: '/exercises/all_exercises/', // Update the URL to match your Django view
            method: 'GET',
            success: function(response) {
                // Clear table rows
                $('#exercise-table tbody').empty();

                // Render exercise data in table
                response.exercises.forEach(exercise => {
                    const row = `<tr>
                        <td>${exercise.date_time}</td>
                        <td>${exercise.duration}</td>
                        <td>${exercise.exercise_name}</td>
                        <td>${exercise.sets}</td>
                        <td>${exercise.reps}</td>
                    </tr>`;
                    $('#exercise-table tbody').append(row);
                });
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    }
});
