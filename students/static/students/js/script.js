
document.addEventListener("DOMContentLoaded", function () {

    // STUDENT SEARCH
    const searchInput = document.getElementById("studentSearch");

    if (searchInput) {
        searchInput.addEventListener("input", function () {

            const searchValue = this.value.toLowerCase();
            const studentItems = document.querySelectorAll(".student-item");

            studentItems.forEach(function (student) {

                const studentName = student.textContent.toLowerCase();

                if (studentName.includes(searchValue)) {
                    student.style.display = "flex";
                } else {
                    student.style.display = "none";
                }

            });

        });
    }

    // PROFILE TABS
    const tabs = document.querySelectorAll(".tab");
    const contents = document.querySelectorAll(".tab-content");

    tabs.forEach(function (tab) {

        tab.addEventListener("click", function () {

            const selectedTab = this.dataset.tab;

            // Remove active class
            tabs.forEach(function (item) {
                item.classList.remove("active");
            });

            contents.forEach(function (content) {
                content.classList.remove("active");
            });

            // Activate selected tab
            this.classList.add("active");

            const selectedContent = document.getElementById(selectedTab);

            if (selectedContent) {
                selectedContent.classList.add("active");
            }

        });

    });

});
