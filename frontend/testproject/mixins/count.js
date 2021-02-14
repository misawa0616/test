export default {
    data() {
        return {
            count: 0,
            temp_test_list: []
        };
    },
    methods: {
        add_temp() {
            this.count += 1;
            this.temp_test_list.push(this.count);
        },
        delete_temp(index) {
            this.temp_test_list.splice(index, 1);
        },
    },
};