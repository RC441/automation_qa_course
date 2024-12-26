from wsgiref.validate import assert_

from pages.interactions_page import SortablePage, SelectablePage, ResizeablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            # print(list_before, list_after)
            # print(grid_before, grid_after)
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"


    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            # print(item_list)
            # print(item_grid)
            assert item_list > 0, "No elements were selected"
            assert item_grid > 0, "No elements were selected"



    class TestResizeablePage:

        def test_resizeable(self, driver):
            resizeable_page = ResizeablePage(driver, "https://demoqa.com/resizable")
            resizeable_page.open()
            max_box, min_box = resizeable_page.change_size_resizeable_box()
            max_resize, min_resize = resizeable_page.change_size_resizeable()
            # print(max_box, min_box)
            # print(max_resize, min_resize)
            assert ('500px', '300px') == max_box, "Maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "Minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "Resizeable has not been changed"


